# Creating Sound Precise models using Association rules learning

Given a log path and set of parameters, the dependency-miner algorithm is responsible for discovering long-term dependencies between the events and results into a precise Petri net which include mined dependencies. Added rules and evaluation metrics are computed and returned.

Call miner(logpath, support, confidence, lift, soundness)
It takes as input
	
        1. logpath (str): Path of event log
        2. support (str): Threshold value for support measure 
        3. confidence (str): Threshold value for confidence measure
        4. lift (str): Threshold value for lift measure, default min value = 1
        5. sound (str) : Soundness requirement if user wants sound model

The resulting precise Petri net can be found in the current location with the same name as that of input event log in .pnml and .svg format

## Installation

```pip install dependency-miner-pm4py```

## How to use it?

Install dependency_miner_pm4py package. Following, from dependency-miner import apply_trans.

        Example: 
        log_path = "<path>\<file>.xes"
        support = "0.2"
        confidence = "0.3"
        lift = "1.0"
        sound = "Yes"
        miner(log_path, support, confidence, lift, sound)

## License

Copyright (c) 2021 Ashwini Jogbhat

This repository is licensed under the MIT license. See LICENSE for details.