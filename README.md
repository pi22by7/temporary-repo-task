# Task - Heydaw Technologies

Python script to controll stuff in Reaper.

## Description

The audio editing tool offers the following functions:

1. **Move Playhead:** `seek_playhead(time: float) -> None`
   This function moves the playhead by the specified amount of time in seconds. A positive value advances the playhead, while a negative value rewinds it.

2. **Duplicate Track:** `duplicate_track(track_index: int) -> None`
   This function duplicates the track at the specified track index in the Reaper project.

3. **Apply ReaGate to Track:** `apply_reagate_to_track(track_index: int) -> None`
   This function applies the ReaGate plugin to the track at the specified track index. If the ReaGate plugin is not already present on the track, it is added.

## Requirements
- Python 3.11
- reapy library (Install it using pip install reapy)
