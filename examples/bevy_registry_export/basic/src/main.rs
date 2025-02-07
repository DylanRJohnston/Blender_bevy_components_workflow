use bevy::prelude::*;
use bevy_editor_pls::prelude::*;
use bevy_gltf_worlflow_examples_common::CommonPlugin;

mod core;
use crate::core::*;

mod game;
use game::*;

mod test_components;
use test_components::*;

fn main() {
    App::new()
        .add_plugins((
            DefaultPlugins.set(AssetPlugin::default()),
            // editor
            EditorPlugin::default(),
            // our custom plugins
            CommonPlugin,
            CorePlugin,           // reusable plugins
            GamePlugin,           // specific to our game
            ComponentsTestPlugin, // Showcases different type of components /structs
        ))
        .run();
}
