# xshell_theme_preview

Generate preview picture from xcs files. https://github.com/netsarang/Xshell-ColorScheme

## File
xcs_loader.py: load values in xcs into database
xshell_theme_preview.py: Generate preview png
selected_pickup.py: copy all selected color schema into `selected` folder
xcs_generator.py: Parse all xcs in selected folder in to one file

## Usage
1. Put all xcs files under the path defined in `XCS_LIB` of `config.py`
2. Kick off `xcs_loader.py` to load all xcs into database
3. Kick off `xshell_theme_preview.py` to generate preview
4. Use below sql to create a favorite list.
```
create table xcs_fav as select 
`index`,
NAME, NULL as is_fav from xcs_profile
```
5. Pick up your favorit color scheme, mark 1 in the `is_fav` column of `xcs_profile`
6. Run `selected_pickup.py` to copy all selected color schema into `selected` folder
7. Run `xcs_generator.py` to generate parsed xcs files as `export_selected.xcs`
8. Import `export_selected.xcs` to Xshell