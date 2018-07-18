Keybindings Note
================

Keybindings.json
----------------

``` json
{
    // editor和terminal切换
    // Toggle between terminal and editor focus
    {
        "key": "ctrl+`",
        "command": "workbench.action.terminal.focus"
    },
    {
        "key": "ctrl+`",
        "command": "workbench.action.focusActiveEditorGroup",
        "when": "terminalFocus"
    }
}
```