## syntaxProfiles.json

this is the Emmet default settings

- <br> — HTML notation
- <br /> — XHTML notation
- <br/> — XML notation

in `Packages/User` 

    mkdir Emmet
    cd Emmet
    touch syntaxProfiles.json

add below

``` json
{
    // force XHTML profile for HTML syntax
    "html": "xhtml",

    // create our own profile for XML
    "xml": {
        "tag_case": "upper",
        "attr_quotes": "single"
    }
}
```
