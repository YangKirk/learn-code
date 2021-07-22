# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     leetcode_1838th
   Description :  
   Author :       kirk
   date：          2021/7/22
-------------------------------------------------
   Change Activity:
                   2021/7/22
-------------------------------------------------
"""
"""
元素的 频数 是该元素在一个数组中出现的次数。

给你一个整数数组 nums 和一个整数 k 。在一步操作中，你可以选择 nums 的一个下标，并将该下标对应元素的值增加 1 。

执行最多 k 次操作后，返回数组中最高频元素的 最大可能频数 。



示例 1：

输入：nums = [1,2,4], k = 5
输出：3
解释：对第一个元素执行 3 次递增操作，对第二个元素执 2 次递增操作，此时 nums = [4,4,4] 。
4 是数组中最高频元素，频数是 3 。
示例 2：

输入：nums = [1,4,8,13], k = 5
输出：2
解释：存在多种最优解决方案：
- 对第一个元素执行 3 次递增操作，此时 nums = [4,4,8,13] 。4 是数组中最高频元素，频数是 2 。
- 对第二个元素执行 4 次递增操作，此时 nums = [1,8,8,13] 。8 是数组中最高频元素，频数是 2 。
- 对第三个元素执行 5 次递增操作，此时 nums = [1,4,13,13] 。13 是数组中最高频元素，频数是 2 。
示例 3：

输入：nums = [3,9,6], k = 2
输出：1


提示：

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
1 <= k <= 10^5
"""


class Solution:
    @staticmethod
    def max_frequency(nums: list, k: int):
        # 如果k >= nums[right] * (right + 1 - left) - window_sum
        # 则max_freq = max(max_freq, right + 1 - left)
        # 如果k < nums[right] * (right + 1 - left) - window_sum
        # 则left +1，right + 1
        n = len(nums)
        if n == 1:
            return 1
        nums.sort()
        left, right, max_freq = 0, 0, 1
        window_sum = sum(nums[left:right])  # window_sum = 0 一开始
        # 滑动窗口
        while right < n:
            # --- 进R
            # print(f'left:{left}, right:{right}, max_freq:{max_freq}')
            # print('window_sum += nums[right]:', window_sum, '+', nums[right])
            window_sum += nums[right]  # window_sum 开始向右增加nums对应的数值
            # ------ 弹L
            # print('nums[right] * (right + 1 - left) - window_sum =',
            #       f'nums[right]:{nums[right]} * right:{right} + 1 - left:{left} ==> '
            #       f'{nums[right] * (right + 1 - left) - window_sum}')
            if k >= nums[right] * (right + 1 - left) - window_sum:
                max_freq = max(max_freq, right + 1 - left)
                # print(f'max_freq:{max_freq}')
            else:
                window_sum -= nums[left]  # 因为补的面积需求超过了k，所以删掉最左边的window_sum
                # print(f'else_window_sum: window_sum:{window_sum} - nums[left]:{nums[left]}')
                left += 1
                # print(f'max_freq:{max_freq}')
            right += 1

        return max_freq


if __name__ == '__main__':
    print(Solution.max_frequency(nums=[1, 4, 8, 13], k=5))
