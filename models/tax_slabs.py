
class Range:
    _is_min_available = bool
    _is_max_available = bool
    _min_price = float()
    _max_price = float()

    def set_min_price(self, price):
        self._min_price = price

    def get_min_price(self):
        return self._min_price

    def set_max_price(self, price):
        self._max_price = price

    def get_max_price(self):
        return self._max_price

    def set_is_min_available(self, flag):
        self._is_min_available = flag

    def get_is_min_available(self):
        return self._is_min_available

    def set_is_max_available(self, flag):
        self._is_max_available = flag

    def get_is_max_available(self):
        return self._is_max_available

    '''Check if a given price is in range'''
    def is_price_in_range(self, price):
        if not self._is_max_available:
            if price > self._min_price:
                return True
            else:
                return False
        elif not self._is_min_available:
            if price <= self._max_price:
                return True
            else:
                return False
        elif self._min_price < price <= self._max_price:
            return True
        return False


class TaxType:
    '''Assuming taxes are of two types (percentage and absolute)'''
    _is_percentage = bool

    def set_is_percentage(self, flag):
        self._is_percentage = flag

    def get_is_percentage(self):
        return self._is_percentage


class TaxSlab:
    _tax_name = int()
    _range = Range()
    _tax = float()
    _type = TaxType()

    def set_tax_name(self, name):
        self._tax_name = name

    def get_tax_name(self):
        return self._tax_name

    def set_tax(self, tax):
        self._tax = tax

    def get_tax(self):
        return self._tax

    def set_type(self, type_str):
        type_tax = TaxType()
        if type_str == "percentage":
            type_tax.set_is_percentage(True)
        else:
            type_tax.set_is_percentage(False)
        self._type = type_tax

    def get_type(self):
        return self._tax

    def set_range(self, min_price, max_price):
        range_tax = Range()
        if min_price is None:
            range_tax.set_is_min_available(False)
        else:
            range_tax.set_is_min_available(True)
            range_tax.set_min_price(min_price)

        if max_price is None:
            range_tax.set_is_max_available(False)
        else:
            range_tax.set_is_max_available(True)
            range_tax.set_max_price(max_price)
        self._range = range_tax

    def get_range(self):
        return self._range

    '''Calculate Tax for each slab'''
    def calculate_tax_for_slab(self, price):
        tax_amount = 0
        if self._range.is_price_in_range(price):
            if self._type.get_is_percentage():
                tax_amount = (self._tax * price) / 100
            else:
                tax_amount = self._tax
        return tax_amount


class TaxSlabs:
    _tax_slab = list()

    def add_tax(self, new_slab):
        self._tax_slab.append(new_slab)

    def get_tax(self):
        return self._tax_slab


    '''Calculate total tax for all slabs'''
    def calculate_total_taxes(self, price):
        total_tax_amount = 0
        for tax_slab in self._tax_slab:
            total_tax_amount += tax_slab.calculate_tax_for_slab(price)
        return total_tax_amount
