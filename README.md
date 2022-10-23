# db_query
Data base query with Python script

:::::::::  :::::::::              ::::::::   :::    ::: :::::::::: :::::::::  :::   :::
:+:    :+: :+:    :+:            :+:    :+:  :+:    :+: :+:        :+:    :+: :+:   :+:
+:+    +:+ +:+    +:+            +:+    +:+  +:+    +:+ +:+        +:+    +:+  +:+ +:+
+#+    +:+ +#++:++#+             +#+    +:+  +#+    +:+ +#++:++#   +#++:++#:    +#++:
+#+    +#+ +#+    +#+            +#+  # +#+  +#+    +#+ +#+        +#+    +#+    +#+
#+#    #+# #+#    #+#            #+#   +#+   #+#    #+# #+#        #+#    #+#    #+#
#########  #########  ##########  ###### ###  ########  ########## ###    ###    ###

- simple script to identify SQLite3 files in a directory
- connect to a chosen database
- list all tables in that database
- list all the rows in chosen table.

## How to use:
- copy raw or clone db_query.py file to your computer.
- check code and, if needed, change .sqlite3 file extensions to .sqlite
- make code executable: $ chmod +x db_query.py
- place it to your scripts directory (for example .bin/)
- write alias in your .zshrc or .bashrc (alias db_query='~/.bin/db_query.py')
- source .zshrc or .bashrc

> now you can use $db_query in your terminal to locate and search 
any SQLite3 database and its tables 
