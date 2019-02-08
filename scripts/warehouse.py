#! /usr/env/bin python3

class Warehouse(object):
    def __init__(self):
        self.items = []
                
        self.psus_unserialized = {}
        self.psus_serialized = {}
        self.psus_filtered = {}

        self.order = []
        self.order_serialized = []

    # Gets the warehouse info as a string, parses it and then maps the itemstrings to ints 
    def init_warehouse_info(self, text):        
        lines = text.split('\n')

        self.items = lines.pop(0).split(' ')

        self.item_to_int_dict = {k: v for v, k in enumerate(sorted(set(self.items)))}
        self.int_to_item_dict = {v: k for k, v in self.item_to_int_dict.items()}

        psu_index = 1
        for line in lines:
            if line != '':
                psu_items = line.strip().split(' ')
                self.psus_unserialized[psu_index] = psu_items
                self.psus_serialized[psu_index] = self.list_serialize(psu_items)
                psu_index += 1

    def init_warehouse_order(self, text):
        order_string = text.strip()
        self.order = order_string.split(' ') 
        self.order_serialized = self.list_serialize(self.order)

    # Maps items in a list to integers based on the item_to_int_dict
    def list_serialize(self, l):
        return [self.item_to_int_dict[item] for item in l]

    # Maps ints in a list back to the their original item name based on the int_to_item_dict
    def list_deserialize(self, l):
        return [self.int_to_item_dict[item] for item in l]

    # Only keep the items of a PSU that are present in the current order
    # and then add them with the old key to a new dict
    def preprocess(self):
        for k, v in self.psus_serialized.items():
            cleaned_items = [x for x in v if x in self.order_serialized]
            if cleaned_items != []:
                self.psus_filtered[k] = cleaned_items

        print("Unserialized PSUs:")
        print(self.psus_unserialized)
        print("Serialized PSUs:")
        print(self.psus_serialized)
        print("Order:")
        print(self.order_serialized)
        print("Original PSUs:")
        print(self.psus_serialized)
        print("Filtered PSUs:")
        print(self.psus_filtered)

