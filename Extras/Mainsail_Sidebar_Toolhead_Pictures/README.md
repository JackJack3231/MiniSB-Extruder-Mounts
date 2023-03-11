# Mainsail Sidebar Toolhead Pictures
Upload the wanted Picture into the `.theme` Folder in `config` folder through Mainsail, and rename the picture to `sidebar-background.png`.

If you don't see a `.theme` folder follow the [Mainsail Documentation](https://docs.mainsail.xyz/features/theming/prepare#theme-folder) to setup the folder.

Because the Pictures have a transparent background you may want to change the background color of the sidebar. To do either edit or add a `custom.css` to your `.theme` folder and add:

```
.v-navigation-drawer__image {
    background: black;
}
```
Of course you can replace black with any color (Name or Hex-Code) you want.
