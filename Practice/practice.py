nums1=[1,2,3,0,0,0]
nums2=[2,3,4]
for i in nums1:
    if i==0:
        nums1.remove(i)
nums1.extend(nums2)
nums1.sort()