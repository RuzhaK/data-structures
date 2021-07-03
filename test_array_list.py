from unittest import TestCase
from array_list import ArrayList

class TestArrayList(TestCase):
    def test_append_when_list_empty_when_value_expect_append_to_the_end(self):
        al=ArrayList()
        al.append(1)
        values=list(al)
        self.assertEqual([1],values)

    def test_append__expect_to_return_the_list(self):
        al=ArrayList()
        result=al.append(1)
        self.assertEqual(al,result)


    def test_append__when_list_not_empty_when_value_expect_append_to_the_end(self):
        al = ArrayList()
        al.append(1)
        al.append(2)
        al.append(3)
        values = list(al)
        self.assertEqual([1,2,3], values)

    def test_append__1024_values__expect_to_append_to_the_end(self):
        al=ArrayList()
        values=[x for x in range(1024)]
        [al.append(x) for x in values]
        list_values=list(al)

        self.assertEqual(values,list_values)

    def test_remove_when_index_is_valid___expect_to_remove_values_and_return_it(self):
        al=ArrayList()

        al.append(1)
        al.append(2)
        al.append(3)
        al.append(4)

        result=al.remove(2)
        self.assertListEqual([1,2,4],list(al))
        self.assertEqual(3,result)

    def test_remove_when_index_is_invalid___expect_to_raise(self):
        al = ArrayList()

        al.append(1)
        al.append(2)
        al.append(3)



        with self.assertRaises(IndexError):
            result = al.remove(al.size())

    def test_get_when_index_is_valid___expect_to_return_it(self):
        al=ArrayList()

        al.append(1)
        al.append(2)
        al.append(3)
        al.append(4)

        result=al.get(2)
        self.assertListEqual([1,2,3,4],list(al))
        self.assertEqual(3,result)
    def test_get_when_index_is_invalid___expect_to_raise(self):
        al = ArrayList()

        al.append(1)
        al.append(2)
        al.append(3)



        with self.assertRaises(IndexError):
            result = al.get(al.size())

    def test_extend__with_empty_iterable_expect_to_be_the_same(self):
        al = ArrayList()

        al.append(1)
        al.extend([])


        self.assertListEqual([1], list(al))


    def test_extend__with_generator_expect_to_append_the_list(self):
        al = ArrayList()

        al.append(1)
        al.extend([x for x in range(1)])

        self.assertListEqual([1, 0], list(al))

    def test_extend__with_list_expect_to_append_the_list(self):

        al = ArrayList()

        al.append(1)
        al.extend([2])

        self.assertListEqual([1,2], list(al))

    def test_extend__with_not_iterable_expect_to_raise(self):
        al = ArrayList()

        al.append(1)


        with self.assertRaises(ValueError):
            al.extend(2)

    def test_extend__when_empty_expect_to_append(self):
        al = ArrayList()

        al.append(1)

        self.assertEqual(list(al),[1])

    def test_insert_when_index_is_valid___expect_to_place_values_and_return_it(self):
        al = ArrayList()

        al.append(1)
        al.append(2)

        al.append(4)
        al.append(5)

        al.insert(2,333)
        self.assertListEqual([1, 2, 333, 4,5], list(al))


    def test_insert_when_index_is_invalid___expect_to_raise(self):
        al = ArrayList()

        al.append(1)
        al.append(2)
        al.append(3)

        with self.assertRaises(IndexError):
            result = al.insert(al.size()+1,2)
    def test_pop__expect_to_remove_last_element_and_return_it(self):
        al=ArrayList()
        al.append(1)
        al.append(2)
        al.append(3)
        al.append(4)

        result=al.pop()
        self.assertEqual(result,4)
        self.assertListEqual([1,2,3],list(al))

    def test_pop__when__empty__expect_to_raise(self):
        al=ArrayList()
        with self.assertRaises(IndexError):
            al.pop()

    def test_clear_expect_to_be_empty(self):
        al=ArrayList()
        [al.append(x) for x in range(15)]
        al.clear()
        self.assertEqual([],list(al))

    def test_index__when_item_is_present_return_correct_index(self):
        al = ArrayList()
        [al.append(x) for x in range(15)]
        index=al.index(5)
        self.assertEqual(5,index)

    def test_index__when_item_is_not_present_raise(self):
        al = ArrayList()
        [al.append(x) for x in range(15)]

        with self.assertRaises(ValueError):
            al.index(17)


    def test_count__when_item_is_present_1_time_return_1(self):
        al = ArrayList()
        [al.append(x) for x in range(15)]
        expected_count=1
        actual_count=al.count(5)
        self.assertEqual(expected_count,actual_count)

    def test_count__when_item_is_present_multiple_times_return_correct_count(self):
        al = ArrayList()
        [al.append(x) for x in range(15)]
        al.insert(3,5)
        al.insert(7,5)
        al.insert(1,5)
        al.insert(9,5)
        al.append(5)

        expected_count = 6
        actual_count = al.count(5)
        self.assertEqual(expected_count, actual_count)

    def test_count__when_item_is_present_multiple_times_and_once_popped_return_correct_count(self):
        al = ArrayList()
        [al.append(x) for x in range(15)]
        al.insert(3,5)
        al.insert(7,5)
        al.insert(1,5)
        al.insert(9,5)
        al.append(5)
        al.pop()
        expected_count = 5
        actual_count = al.count(5)
        self.assertEqual(expected_count, actual_count)

    def test_count__when_item_is_not_present_return_0(self):
        al = ArrayList()
        expected_count = 0
        actual_count = al.count(5)
        self.assertEqual(expected_count, actual_count)

    def test_reverse__expect_in_reversed_order(self):
        al = ArrayList()
        [al.append(x) for x in range(5)]
        expected=[x for x in range(4,-1,-1)]
        actual=al.reverse()

        self.assertEqual(expected,actual)

    def test_copy__expect_to_return_another_list_with_same_values(self):
        al = ArrayList()
        [al.append(x) for x in range(5)]
        copied_list=al.copy
        expected=[x for x in range(5)]

        self.assertNotEqual(copied_list,al)
        self.assertEqual(expected,list(al))

    def test_add_first_when_empty__expect_to_add(self):
        al = ArrayList()
        al.add_first(1)
        self.assertEqual([1], list(al))

    def test_add_first_when_not_empty__expect_to_add(self):
        al = ArrayList()
        [al.append(x) for x in range(5)]
        al.add_first(1)

        self.assertEqual([1,0,1,2,3,4], list(al))

    def test_dictionize__when_empty__expect_empty_dict(self):
        al = ArrayList()
        actual=al.dictionize()
        expected= {}

        self.assertDictEqual(actual,expected)

    def test_dictionize__when_even_elements__expect_correct_result(self):
        al = ArrayList()
        al.append(1)
        al.append(2)
        al.append(3)
        al.append(4)
        actual = al.dictionize()
        expected = {
            1:2,
            3:4,
        }

        self.assertDictEqual(actual, expected)
    def test_dictionize__when_odd_elements__expect_correct_result(self):
        al = ArrayList()
        al.append(1)
        al.append(2)
        al.append(3)

        actual = al.dictionize()
        expected = {
            1: 2,
            3: " ",
        }

        self.assertDictEqual(actual, expected)

    def test_move__when_list_empty__expect_to_move_nothing(self):
        al = ArrayList()
        al.move(1)

        self.assertListEqual([],list(al))

    def test_move__when_moving_1_element__expect_to_move_element_to_the_end(self):
        al = ArrayList()
        [al.append(x) for x in range(5)]
        al.move(1)

        self.assertListEqual([1,2,3,4,0],list(al))

    def test_move__when__moving_3_elements_and_have_2_elements__expect_to_move_elements_to_the_end(self):
        al = ArrayList()
        [al.append(x) for x in range(1,3)]
        # 1,2>1,2>2,1
        al.move(3)

        self.assertListEqual([2, 1], list(al))

    def test_overbound__expect_to_return_max_element(self):
        al = ArrayList()
        values = [x for x in range(15)]
        [al.append(x) for x in values]
        expected = max(values)
        actual = al.overbound()

        self.assertEqual(expected, actual)

    def test_underbound__expect_to_return_min_element(self):
        al = ArrayList()
        values= [x for x in range(15)]
        [al.append(x) for x in values]
        expected=min(values)
        actual=al.underbound()

        self.assertEqual(expected,actual)










