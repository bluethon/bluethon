``` json
{
    "build_systems":
    [
        {
            "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
            "name": "Anaconda Python Builder",
            "selector": "source.python",
            // $project_path 设置当前项目路径
            // http://docs.sublimetext.info/en/latest/reference/build_systems/configuration.html
            "shell_cmd": "\"$project_path/venv/bin/python3\" -u \"$file\""
        }
    ],
    "folders":
    [
        {
            "folder_exclude_patterns":
            [
                "venv"
            ],
            "path": "."
        },
        {
            "path": "/home/blue/github/bluethon"
        }
    ],
    "settings":
    {
        // anaconda configuration
        "python_interpreter": "./venv/bin/python3",
        
        "test_command": "python -m unittest discover",
        "validate_imports": true
    }
}
```
