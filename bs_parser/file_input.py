#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 18:33:01 2020

@author: drew
"""
import bs4 as bs
import lxml
from lxml import etree as et
from bs_parser.models import UnitProfile

class XmlParser:
    path = "/home/drew/Downloads/"
    file_name = "admech.ros"
    
    def __init__(self):
        file = open(self.path + self.file_name, 'r')
        contents = file.read()
        
        soup = bs.BeautifulSoup(contents, 'lxml')
        reduced_soup = self.find_all_units(soup)
        self.get_unit_profile(reduced_soup)
            
    def find_all_units(self, tag):
        unit = tag.find_all(type="model")
        return unit
    
    def get_unit_profile(self, reduced_soup):
        for unit in reduced_soup:
            profile = unit.profiles.profile
            name = profile['name']
            characteristics = profile.find_all('characteristic')
#            if len(characteristics) == 9:
#                movement = characteristics[0].get_text()
#                weapon_skill = characteristics[1].get_text()
#                ballistic_skill = characteristics[2].get_text()
#                strength = characteristics[3].get_text()
#                toughness = characteristics[4].get_text()
#                wounds = characteristics[5].get_text()
#                attacks = characteristics[6].get_text()
#                leadership = characteristics[7].get_text()
#                save = characteristics[8].get_text()
            
            for character in characteristics:
                name = character['name']
                if name == 'M':
                    move = character.get_text()
                if name == 'WS':
                    weapon_skill = character.get_text()
                if name == 'BS':
                    ballistic_skill = character.get_text()
                if name == 'S':
                    strength = character.get_text()
                if name == 'T':
                    toughness = character.get_text()
                if name == 'W':
                    wounds = character.get_text()
                if name == 'A':
                    attacks = character.get_text()
                if name == 'LD':
                    leadership = character.get_text()
                if name == 'Save':
                    save = character.get_text()
            unit = UnitProfile.create(name, move, weapon_skill, ballistic_skill,
                                      strength, toughness, wounds, attacks,
                                      leadership, save)
            unit.save()
        
if __name__=="__main__":
    XmlParser()
    