# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_get_name(self):
        items = [Item("foo", 1, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)
        
    # Standard/All Items
    def test_decrement_quality_of_standard_item_by_1(self):
        items = [Item("foo", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].quality)

    def test_decrement_sell_in_of_standard_item_by_1(self):
        items = [Item("foo", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)

    def test_decrement_sell_in_of_negative_standard_item_by_1(self):
        items = [Item("foo", -1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-2, items[0].sell_in)

    def test_decrement_quality_of_standard_item_by_2_after_sell_in(self):
        items = [Item("foo", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(8, items[0].quality)

    def test_catch_exception_quality_cant_be_more_than_50(self):
        with self.assertRaises(Exception) as context:
            items = [Item("foo", 10, 80)]
            gilded_rose = GildedRose(items)
            gilded_rose.update_quality()
        self.assertTrue('The Quality of an item is never more than 50!' in context.exception)

    def test_catch_exception_quality_cant_be_less_than_0(self):
        with self.assertRaises(Exception) as context:
            items = [Item("foo", 20, -1)]
            gilded_rose = GildedRose(items)
            gilded_rose.update_quality()
        self.assertTrue('The Quality of an item is never less than 0!' in context.exception)
    
    def test_catch_exception_quality_cant_be_decremented_less_than_0(self):
        items = [Item("foo", 20, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    # Sulfurus
    def test_NOTdecrement_quality_of_sulfurus(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 20, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)

    def test_NOTdecrement_sell_in_of_sulfurus(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(10, items[0].sell_in)

    def test_catch_exception_quality_of_sulfurus_must_be_80(self):
        with self.assertRaises(Exception) as context:
            items = [Item("Sulfuras, Hand of Ragnaros", 20, 79)]
            gilded_rose = GildedRose(items)
            gilded_rose.update_quality()
        self.assertTrue('The Quality of Sulfurus is always exactly 80!' in context.exception)

    # Aged Brie
    def test_increment_quality_of_aged_brie_by_1(self):
        items = [Item("Aged Brie", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(11, items[0].quality)

    def test_decrement_sell_in_of_aged_brie_by_1(self):
        items = [Item("Aged Brie", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)

    # Backstage passes
    def test_increment_quality_of_backstage_passes_by_2_when_sell_in_between_10_and_6(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(7, items[0].quality)

    def test_increment_quality_of_backstage_passes_by_3_when_sell_in_between_5_and_1(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(13, items[0].quality)

    def test_decrement_quality_of_backstage_passes_to_0_when_sell_in_is_0(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    # Conjured
    def test_decrement_quality_of_conjured_item_by_2(self):
        items = [Item("Conjured Mana Cake", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(18, items[0].quality)

        

        
if __name__ == '__main__':
    unittest.main()
