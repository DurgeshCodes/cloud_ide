# core/terminal/core.py

import os
import pty
import asyncio
import threading


class TerminalProcess:
    def __init__(self, cwd, on_output_async, loop=None):
        self.loop = loop or asyncio.get_event_loop()
        self.on_output_async = on_output_async
        self.master_fd, slave_fd = pty.openpty()

        self.pid = os.fork()
        if self.pid == 0:
            os.chdir(cwd)
            os.setsid()
            os.dup2(slave_fd, 0)
            os.dup2(slave_fd, 1)
            os.dup2(slave_fd, 2)

            # Start clean shell without loading ~/.bashrc or ~/.profile
            os.execvp("bash", ["bash", "--noprofile", "--norc"])
        else:
            self.running = True
            self.thread = threading.Thread(target=self._read_loop, daemon=True)
            self.thread.start()

    def _read_loop(self):
        while self.running:
            try:
                output = os.read(self.master_fd, 1024)
                asyncio.run_coroutine_threadsafe(
                    self.on_output_async(output), self.loop
                )
            except Exception:
                break

    def write(self, data):
        os.write(self.master_fd, data.encode())

    def stop(self):
        self.running = False
        os.kill(self.pid, 15)
