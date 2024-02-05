Basics
- [x] add panel
- [x] add a "create blueprint" button
    - [x] when clicked: 
        - [x] create collection 
        - [x] add an empty inside collection and name it <COLLECTION_NAME>_components
        - [x] add a **AutoExport** Boolean property to collection 
        - [x] add name imput(popup for name input ?)

- [x] add a list of existing components/custom properties
- [x] add an "edit blueprint" section
    - [x] only filled when there is ONE selection, and that selection is a collection
    - [x] add a dropdown of possible components  
    - [x] add a checkbox for enabling disabling a component (enabled by default)
    - [x] add a button for copying a component
    - [x] add a button for pasting a component


UI:
 - [x] filterable list of components to DISPLAY for selection : ComponentDefinitionsList

- Filter out invalid objects for components that have no _components suffix ? (that is too limiting I think)
- -[x] How to deal with pre-existing custom properties that have NO metadata
    * if there is one without metadata: find if there is an available component with the same name & type ?
    * if there is , insert metadata
    * otherwise, mark it in some way visually ?

- [x] for OBJECT enums: add two ui pieces
    - [x] one for selecting the TYPE to choose (ie normal enum)
    - [x] one for setting the VALUE inside that


- [x] vecs => (not vec2, vec3 etc) more complex UI to add items in a list
    - [x] generate contained CollectionGroup
    - [x] CollectionProperty => type = the above
- [x] find ways to "collapse" the different levels of nested data of structs/tupples into a single custom property (ideally on the fly, but we can do without)

- [x] for single tupple components that represent a single unit type, re_use the base type's UIPropertyGroup instead of creating specific ones (ie TuppleTestF32_ui...) => will not work, would cause overriden "update callback"
- [x] pre_generate default values/values for each main type

- [x] fix issues with vec2 etc not having the correct number of items
- [x] fix bad defaults in ui group
- [x] fix object enums handling on updates (??)
- [x] fix issues with lambads in loops

- [x] object enum should be <EntryName>(params)
    ie  *Collider:
            * Cuboid(Vec3)
            * Sphere(radius)
- [x] deal with enums variants that do not have any data: ex   {
          "title": "Mesh"
        }

- [x] remove / change use of ComponentDefinitionsList 
    - when filling the list, use the long_name as index ie items.append((str(index), item.name, item.long_name)) => items.append((item.long_name, item.name, item.long_name))
- [x] when removing a component, reset the value of the attribute in the property group (or not ? could be a feature)
- [x] deal correctly with fields of types that are NOT in the schema.json (for ex PlayingAnimation in AnimationPlayer)
- [ ] deal correctly with complex types 
            CascadeShadowConfig: has an array/list
            ClusterConfig: one of the enum variants is an object
- [ ] possibly allow Color to be an enum as it should be ?
- [x] for sub items , the update functions "Name" should be the one of the root object
- [x] fix copy & pasting
    - it actually works, but the value of the custom property are not copied back to the UI, need to implement property_group_value_from_custom_property_value
- [ ] we need a notion of "root propertyGroup" =?
- [x] notify user of missing entries in schema (ie , unregistered data types)
- [x] clarify propgroup_ui vs named nested fields
- [x] fix basic enums handling
- [x] add a list of not found components to the registry, add to them on the fly
- [x] add configuration panel (open the first time, closed on further user once configured)

- [x] add limits to ixxx types vs utypes
- [x] only display the "generate components xx" when relevant ie:
    - go through list of custom properties in current object
        - if one does not have metadata and / or propgroup: 
            break 

- [x] remove custom property of disabled component ? => NOpe, as we need custom properties to iterate over
- [x] what to do with components with n/a fields ? perhaps disable the component ? add a "invalid" field to meta ?
- [x] format output as correct RON
    - [x] fix issue with empty strings
- [x] change custom property => propGroup to convert RON => Json first => obsolete
- [x] cleanup process_lists

- [x] fix issues with enum variants with only a title

- [x] display single item enums inline, others in a seperate row

- [x] add button to "apply all" (in configuration), to apply/update all custom properties to ALL objects where relevant
- [x] add button to "apply to current" to do the same with current
- [x] add warning sign to the above

- [x] what about metadata ?
- [x] only upgrade custom properties to metadata when asked/relevant
- [x] implement move list up/down
- [ ] change property_group_value_from_custom_property_value => just disregard it for now, its point is very limited (helping people with old custom properties by attempting to generate real values)
    and give the change to a real ron format, it is too limiting
- [x] fix reload registry clearing list of missing types 
- [x] clean up metadata module, a lot of repeated code
- [x] some fields when original is 0 or 0.0 are not copyable ? (seems like a bad boolean check )
- [x] fix issues with object variants in enums (see clusterconfig)


- perhaps directly export default values within the schema.json ?
        - for most types , it is straighforward, but others, not so much: like the default color in Bevy , etc

- [x] change default schema.json to registry.json
- [x] pasted components do not get updated value in custom_property
- [x] finish documentation
- [x] add storage of registry path
    - [x] save after setting the data (browse for)
    - [x] load after each reload ?

# Additional
    - [x] check if output "string" in custom properties are correct

    - gltf_auto_export
        - [ ] add support for "enabled" flag
        - [ ] add special components 
                - "AutoExport" => Needed
                - "Dynamic" ? naah wait that should be exported by the Bevy side
        - [ ] filter out Components_meta ??
        - [x] add legacy mode to the persisted parameters

    - bevy_gltf_components:
        - [x] first release patch for current issues
        - [x] make configurable 
        - [x] add "compatibility mode" and deprecation warnings for the current hack-ish conversion of fake ron
        - [x] update docs to show we need to use ComponentsFromGltfPlugin::default

    - bevy_gltf_blueprints
        - [x] update dependency
        - [x] update version
        - [x] add ability to set legacy mode for bevy_gltf_components ? 

    - [ ] release all versions
    - [ ] update main documentation, add compatibility version grid

    