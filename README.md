# xshell_theme_preview

Generate preview picture from xcs files. https://github.com/netsarang/Xshell-ColorScheme

## File
xcs_loader.py: load values in xcs into database
xshell_theme_preview.py: Generate preview png 

## Usage
1. Put all xcs files under the path defined in `XCS_LIB` of `config.py`
2. Kick off `xcs_loader.py` to load all xcs into database
3. Kick off `xshell_theme_preview.py` to generate preview



Use below sql to create a favorite list.
```
create table xcs_fav as select 
`index`,
NAME, NULL as is_fav from xcs_profile
```