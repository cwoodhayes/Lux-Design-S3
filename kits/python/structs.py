"""structure of the observation dictionary

laying this out here because I want auto-complete to help me
"""

import dataclasses
import numpy as np

"""
// T is the number of teams (default is 2)
// N is the max number of units per team
// W, H are the width and height of the map
// R is the max number of relic nodes
{
  "obs": {
    "units": {
      "position": Array(T, N, 2),
      "energy": Array(T, N, 1)
    },
    // whether the unit exists and is visible to you. units_mask[t][i] is whether team t's unit i can be seen and exists.
    "units_mask": Array(T, N),
    // whether the tile is visible to the unit for that team
    "sensor_mask": Array(W, H),
    "map_features": {
        // amount of energy on the tile
        "energy": Array(W, H),
        // type of the tile. 0 is empty, 1 is a nebula tile, 2 is asteroid
        "tile_type": Array(W, H)
    },
    // whether the relic node exists and is visible to you.
    "relic_nodes_mask": Array(R),
    // position of the relic nodes.
    "relic_nodes": Array(R, 2),
    // points scored by each team in the current match
    "team_points": Array(T),
    // number of wins each team has in the current game/episode
    "team_wins": Array(T),
    // number of steps taken in the current game/episode
    "steps": int,
    // number of steps taken in the current match
    "match_steps": int
  },
"""


@dataclasses.dataclass(frozen=True)
class Observation:
    units_position: np.ndarray
    units_energy: np.ndarray
    units_mask: np.ndarray
    sensor_mask: np.ndarray
    map_features_energy: np.ndarray
    map_features_tile_type: np.ndarray
    relic_nodes_mask: np.ndarray
    relic_nodes_position: np.ndarray
    team_points: np.ndarray
    team_wins: np.ndarray
    steps: int
    match_steps: int

    _obs: dict

    @classmethod
    def from_obs(cls, obs: dict) -> "Observation":
        return cls(
            units_position=np.array(obs["units"]["position"]),
            units_energy=np.array(obs["units"]["energy"]),
            units_mask=np.array(obs["units_mask"]),
            sensor_mask=np.array(obs["sensor_mask"]),
            map_features_energy=np.array(obs["map_features"]["energy"]),
            map_features_tile_type=np.array(obs["map_features"]["tile_type"]),
            relic_nodes_mask=np.array(obs["relic_nodes_mask"]),
            relic_nodes_position=np.array(obs["relic_nodes"]),
            team_points=np.array(obs["team_points"]),
            team_wins=np.array(obs["team_wins"]),
            steps=obs["steps"],
            match_steps=obs["match_steps"],
            _obs=obs,
        )


@dataclasses.dataclass(frozen=True)
class GivenEnvironmentParams:
    """
    Info we're given for each game
    """

    max_units: int
    match_count_per_episode: int
    max_steps_in_match: int
    map_height: int
    map_width: int
    num_teams: int
    unit_move_cost: int
    unit_sap_cost: int
    unit_sap_range: int
    unit_sensor_range: int
