# -*- coding: utf-8 -*-

import sys
import time


# This object relies on sys._getframe() to collect runtime data. While
# a protected function, numerous modules from the standard library such
# as inspect, logging, and traceback all ultimately rely it as well. A
# handful of top-rated Stack Overflow answers concur [1].
# sys._getframe() as such is idiomatic, stable, and arguably canonical.
#
# See Also
# --------
# inspect.stack()
# logging.Logger.findCaller()
# traceback.format_stack()
#
# References
# ----------
# .. [1] Albert Vonpupp, "How to get a function name as a string in
#    Python?", http://stackoverflow.com/a/13514318/6754214
class Tracer:

    def __init__(self, next_frame_name):

        """
        Context manager for collecting runtime data.

        See the README section on Examples for more details.

        Parameters
        ----------
        next_frame_name : str
            This generally refers to the name of the method or
            function being called within the context manager.
        """

        self._next_frame_name = next_frame_name
        # A depth of 0 returns the frame at the top of the call stack.
        # An offset is therefore required to account for calling the
        # Tracer itself.
        self._current_frame = sys._getframe(1)
        self._previous_frame = sys._getframe(2)
        self._start_time = None
        self._stop_time = None

    def to_json(self):

        """
        Convert the object into a serializable primitive.

        Returns
        -------
        dict
        """

        data = {
            'next_frame_name': self._next_frame_name,
            'current_frame_file_path': self._current_frame.f_code.co_filename,
            'current_frame_line_number': self._current_frame.f_lineno,
            'current_frame_name': self._current_frame.f_code.co_name,
            'previous_frame_file_path': self._previous_frame.f_code.co_filename,
            'previous_frame_line_number': self._previous_frame.f_lineno,
            'previous_frame_name': self._previous_frame.f_code.co_name,
            'start_time': self._start_time,
            'stop_time': self._stop_time}

        return data

    def __enter__(self):
        self._start_time = time.time()
        return self

    # Upon exiting the context, this method is passed the exception
    # type, value, and stacktrace if they exist.
    def __exit__(self, *args, **kwargs):
        self._stop_time = time.time()

    def __repr__(self):
        repr_ = '{}(next_frame_name="{}")'
        return repr_.format(self.__class__.__name__, self._next_frame_name)

