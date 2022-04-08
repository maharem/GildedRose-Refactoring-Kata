# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        self.decrement_quality_by_one(item)
            else:
                if item.quality < 50:
                    self.increment_quality_by_one(item)
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                self.increment_quality_by_one(item)
                        if item.sell_in < 6:
                            if item.quality < 50:
                                self.increment_quality_by_one(item)
            if item.name != "Sulfuras, Hand of Ragnaros":
                self.decrement_sell_in_by_one(item)
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                self.decrement_quality_by_one(item)
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        self.increment_quality_by_one(item)

    def decrement_sell_in_by_one(self, item):
        item.sell_in = item.sell_in - 1

    def if_(self, item):
        item.quality = item.quality + 1


    def increment_quality_by_one(self, item):
        item.quality = item.quality + 1

    def decrement_quality_by_one(self, item):
        item.quality = item.quality - 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    
