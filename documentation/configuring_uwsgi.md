#### Must Set
##### `shared-socket`
- Use a privileged port.
- This option is usually applied in tandem with `sudo --preserve-env` and `--http`. See also `http`.
##### `http`
- Start an HTTP server at the specified hostname and port, or socket number.
- `--http-socket` should not be used if clients will be communicating directly with uWSGI. This option is usually
applied in tandem with `--shared-socket`. See also `shared-socket` and the
[source documentation](http://uwsgi-docs.readthedocs.io/en/latest/ThingsToKnow.html).
##### `module`
- File path containing the application object or callable.
- The path may be qualified using dot notation. `--file` or `--wsgi-file` should not be used because they are less
flexible. This option is usually applied in tandem with `--callable`. See also `callable`.
##### `callable`
- Application object or a callable returning the application object.
- This option is usually applied in tandem with `--module`. See also `module`.

#### Should Set
##### `uid`
- Change the privileges to the specified user.
- This option is usually applied in tandem with `--gid`. See also `gid`.
##### `gid`
- Change the privileges to the specified group.
- This option is usually applied in tandem with `--uid`. See also `uid`.
##### `logto`
- File path to which log records will be written.
- The file permissions are not affected by `uid` or `gid`.
##### `logfile-chown`
- Change the log file permissions.
- The is functionally similar but clearer than `logto2`. Depends on `logto`, `uid`, and `gid`.
##### `enable-threads`
- Use threads and most importantly the global interpreter lock (GIL).
##### `vacuum`
- Try to clean up the temporary files and sockets that were created at runtime.

#### Could Set
##### `chdir`
- Working directory from which to load the application.
- See also `module` and `callable`.
##### `die-on-term`
- See also the [source documentation](http://uwsgi-docs.readthedocs.io/en/latest/ThingsToKnow.html).
##### `need-app`
- Exit if the application cannot be loaded successfully.
##### `show-config`
- Write the configuration to the output.

#### Could Set (In Development Only)
##### `plugin-list`
##### `print`

#### Won't Set
##### `harakiri`
##### `http-gid`
##### `http-processes`
##### `http-threads`
##### `http-timeout`
##### `http-uid`
##### `lazy-apps`
##### `logto2`
##### `master`
##### `memory-report`
##### `need-plugin`
- Exit if the plugin cannot be loaded successfully.
- See also `plugin`.
##### `plugin`
- The `http` and `python` plugins are embedded when uWSGI is installed using `pip`.
- See also `need-plugin`.
##### `processes`
##### `single-interpreter`
##### `strict`
##### `threads`
##### `thunder-lock`
##### `touch-reload`
