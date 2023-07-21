import reapy


def move_playhead(time: float) -> None:
    """
    Description: This function moves the playhead by the specified amount of time in seconds.
                 A positive value advances the playhead, while a negative value rewinds it.

    Input Parameters:
    time (float) - The amount of time in seconds to move the playhead.

    Return Parameter:
    None
    """
    project = reapy.Project()
    try:
        time = float(time)
        current_position = project.cursor_position
        project.cursor_position = current_position + time
    except ValueError:
        print(
            "Error: Invalid time value. Please provide a valid floating-point number."
        )
        return None


def duplicate_track(track_index: int) -> None:
    """
    Description: This function duplicates the track at the specified track index.

    Input Parameters:
    track_index (int) - The index of the track to be duplicated.

    Return Parameter:
    None
    """
    project = reapy.Project()
    try:
        track_index = int(track_index)
        original_track = project.tracks[track_index]

        for track in project.tracks:
            track.selected = False
        original_track.selected = True

        project.perform_action(40062)

    except (ValueError, IndexError):
        print("Error: Invalid track index. Please provide a valid integer track index.")
        return None


def apply_reagate_to_track(track_index: int) -> None:
    """
    Description: This function applies the ReaGate plugin to the track at the specified track index.
                 If the ReaGate plugin is not already present on the track, it is added.

    Input Parameters:
    track_index (int) - The index of the track to which ReaGate will be applied.

    Return Parameter:
    None
    """
    project = reapy.Project()
    try:
        track_index = int(track_index)
        track = project.tracks[track_index]
        gate_found = False

        for fx in track.fxs:
            if fx.name == "VST: ReaGate (Cockos)":
                gate_found = True
                break

        if not gate_found:  # If ReaGate is not present, add it to the track
            fx = track.add_fx("ReaGate (Cockos)")

        gate_params = {  # Define initial parameters
            "Threshold": -20.0,
            "Attack": 10,  # Fast attack
            "Release": 330,  # Slow release
            "Noise level": -60,
            "Dry": -20.0,
            "Wet": 0.0,
        }
        # Set the plugin parameters
        # The initialized values will be wrong graphically since they are not normalized
        for (param_name, param_value) in gate_params.items():
            fx.params[param_name] = param_value

    except (ValueError, IndexError):
        print("Error: Invalid track index. Please provide a valid integer track index.")
        return None


# Test the functions
move_playhead(10)
# duplicate_track(0)
# apply_reagate_to_track(1)
