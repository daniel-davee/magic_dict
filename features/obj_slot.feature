@magic_dict @obj_slot
Feature: passing an object to MagicDict(obj), will now allow magic_dict() to retrive obj
  Scenario: construct a MagicDict passing 3 
    Given input to MagicDict is 3 as int 
      When magic_dict is called
      Then the result is 3 as int