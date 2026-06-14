# Geometry Knowledge Framework

## Observation

Many autonomous vehicle systems rely on:

- HD maps
- Cameras
- LiDAR
- Radar

However, HD maps require continual maintenance and can become outdated due to:

- construction
- lane shifts
- temporary traffic control
- infrastructure changes

## Concept

Instead of treating roadway geometry as a static map, use it as a stable transportation reference framework.

Examples:

- roadway curvature
- route alignment
- Linear Referencing System (LRS)
- mile markers
- interchanges
- ramps
- speed transitions
- roadway classification

These characteristics typically change far less frequently than lane markings or temporary construction.

## Proposed Approach

Use:

Geometry Knowledge + Live Sensor Reality

rather than:

Static HD Map + Live Sensor Reality

The geometry layer provides context while the perception system determines current roadway conditions.

## Example

The vehicle may know:

- approaching interchange
- high-curvature segment ahead
- speed transition zone
- historically complex merge area

while cameras, LiDAR, and radar determine:

- current lane locations
- temporary barriers
- construction activity
- traffic conditions

## Research Question

Can roadway geometry, linear referencing systems, and transportation network characteristics provide a stable contextual framework that complements live perception systems while reducing dependence on fully pre-mapped HD environments?

## Future Data Sources

- FDOT LRS Routes
- FDOT Mile Markers
- FDOT AADT
- FDOT Speed Limits
- FDOT Interchanges
- FDOT Ramps
- FDOT Signals
- LiDAR-derived roadway geometry

## Status

Concept under investigation.
No performance claims have been validated.
Future prototypes will explore geometry-aware contextual reasoning using transportation datasets.