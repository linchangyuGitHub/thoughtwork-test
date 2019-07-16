#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import getopt


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


class Solution(object):
    def __init__(self):
        # Entity Class for File Reading
        self.file_obj = None
        # Mapping of Roman Numbers to Arabic Numbers
        self.roman_number_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        # Recording the value of three materials
        self.material_credits = {
            "Silver": 0,
            "Gold": 0,
            "Iron": 0
        }
        # Mapping of Intergalactic Numbers to Roman Numbers
        self.intergalactic_roman_dict = {}

    def main(self, argv=None):
        """

        Open the test file and initialize an entity class of file type.
        If the file does not exist, the error log is printed and returned.

        Args:
            argv=None

        Returns:
            None

        Raises:
            IOError: An error occurred accessing the bigtable.Table object.
        """
        if argv is None:
            argv = sys.argv
        try:
            try:
                # Files "testinput.txt" should be in the same path as py files
                cur_dir = (os.path.dirname(os.path.realpath(__file__))).replace("\\", "/")
                cur_dir += "/" + "testinput.txt"
                self.file_obj = open(cur_dir)
                if self.file_obj:
                    self.solution()
                else:
                    print "testinput.txt is Missing, " \
                          "Please place the testinput.txt in the directory where the current file is located."
            except getopt.error, msg:
                raise Usage(msg)
        except Usage, err:
            print >>sys.stderr, err.msg
            return 2

    def solution(self):
        """

        Read file information line by line and process it differently according to content.
        Save or compute different values according to the contents of the read file and output them.

        Args:
            None

        Returns:
            None

        Raises:
            IOError: An error occurred accessing the bigtable.Table object.
        """
        line = self.file_obj.readline().strip('\n')
        while line:

            temp_line = line
            temp_list = temp_line.split(" ")
            temp_len = len(temp_list)
            line = self.file_obj.readline().strip('\n')

            if temp_len < 3:
                if self.intergalactic_roman_dict != {}:
                    self.printResult([], -1)
                continue

            if temp_list[1] == "is" and temp_list[2] in self.roman_number_dict:
                self.intergalactic_roman_dict[temp_list[0]] = temp_list[2]

            elif temp_list[temp_len-1] == "Credits" and temp_list[temp_len-3] == "is":
                self.calMaterialCredits(temp_list)

            elif str(temp_line).startswith("how much is ") and str(temp_line).endswith("?"):
                list_reduce = temp_list[temp_list.index("is") + 1:temp_list.index("?")]
                val = self.intergalacticToArabic(list_reduce)
                self.printResult(list_reduce, val)

            elif str(temp_line).startswith("how many Credits is ") and str(temp_line).endswith("?"):
                list_reduce = temp_list[temp_list.index("is") + 1:temp_list.index("?") - 1]
                material_type = self.getMaterialType(temp_list)
                if material_type == "":
                    self.printResult([], -1)
                    continue

                val = self.intergalacticToArabic(list_reduce)
                if val == -1:
                    self.printResult([], -1)
                    continue

                res = val * self.material_credits[material_type]
                self.printResult(list_reduce, res, material_type + " ", " Credits")

            else:
                self.printResult([], -1)

    def calMaterialCredits(self, material_list):
        """

        Calculate the value of different materials and save them in an initialized dictionary.

        Args:
            material_list: list, Including intergalactic numbers and material type.

        Returns:
            None

        Raises:
            IOError: An error occurred accessing the bigtable.Table object.
        """
        total_credits = float(material_list[len(material_list) - 2])
        material_type = self.getMaterialType(material_list)
        if material_type == "":
            return
        list_reduce = material_list[:material_list.index("is") - 1]
        val = self.intergalacticToArabic(list_reduce)
        if val != -1:
            self.material_credits[material_type] = total_credits / val


    def intergalacticToArabic(self, intergalactic_list):
        """

        Convert intergalactic numerals to Arabic numerals.

        Args:
            intergalactic_list: list, Including intergalactic numbers .

        Returns:
            arabic_num:int, an Integer Number.

        Raises:
            IOError: An error occurred accessing the bigtable.Table object.
            if any exception occurred, the function will return -1
        """
        if intergalactic_list is None or len(intergalactic_list) == 0:
            return -1
        try:
            roman_str = ""
            for item in intergalactic_list:
                if item in self.intergalactic_roman_dict:
                    roman_str += self.intergalactic_roman_dict[item]
                else:
                    return -1
            arabic_num = 0
            length = len(roman_str)
            for item in range(length):
                if item < length - 1 and \
                        self.roman_number_dict[roman_str[item]] < self.roman_number_dict[roman_str[item + 1]]:
                    arabic_num -= self.roman_number_dict[roman_str[item]]
                else:
                    arabic_num += self.roman_number_dict[roman_str[item]]
            return arabic_num
        except Usage, err:
            print >> sys.stderr, err.msg
            return -1

    def printResult(self, res_list, res_val, material="", credits=""):
        """

        A wrapped function for outputting results.

        Args:
            res_list: list, Including intergalactic numbers .
            res_val: int, the number of result. When this args is -1, it means a Unexpected situation.
            material: str, material_type. The default is empty.
            credits: str, credits.The default is empty.
        Returns:
            None

        Raises:
            IOError: An error occurred accessing the bigtable.Table object.
        """
        if res_val == -1:
            print "I have no idea what you are talking about"
        else:
            result = ""
            for item in res_list:
                result += item + " "
            print result + material + "is " + str(int(res_val)) + credits

    def getMaterialType(self, material_list):
        """

        Get the material type from the current line of the read-in file.

        Args:
            material_list: list, Including intergalactic numbers .
        Returns:
            material_type: str, Gold/Selver/Iron.

        Raises:
            IOError: An error occurred accessing the bigtable.Table object.
            if any exception occurred, the function will return ""
        """
        if "Gold" in material_list:
            if "Silver" not in material_list and "Iron" not in material_list:
                return "Gold"
            else:
                return ""
        if "Silver" in material_list:
            if "Gold" not in material_list and "Iron" not in material_list:
                return "Silver"
            else:
                return ""
        if "Iron" in material_list:
            if "Silver" not in material_list and "Gold" not in material_list:
                return "Iron"
            else:
                return ""
        return ""


if __name__ == "__main__":
    solution = Solution()
    sys.exit(solution.main())
