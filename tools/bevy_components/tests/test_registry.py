import bpy


def test_blend():
    registry = bpy.context.window_manager.components_registry
    registry.schemaPath = "../../testing/bevy_registry_export/basic/assets/registry.json"
    bpy.ops.object.reload_registry()
    #print("registry type infos", registry.type_infos)

    short_name = "BasicTest"
    component_type = registry.short_names_to_long_names[short_name]

    add_component_operator = bpy.ops.object.add_bevy_component
    add_component_operator(component_type=component_type)

    property_group_name = registry.get_propertyGroupName_from_shortName(short_name)
    object = bpy.context.object

    target_components_metadata = object.components_meta.components
    component_meta = next(filter(lambda component: component["name"] == short_name, target_components_metadata), None)
    propertyGroup = getattr(component_meta, property_group_name, None)
    print("propertyGroup", propertyGroup, propertyGroup.field_names)


    """copy_component_operator = bpy.ops.object.copy_bevy_component
    copy_component_operator()"""


    assert propertyGroup.field_names == ['a', 'b', 'c']