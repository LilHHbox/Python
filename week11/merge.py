# Author: Lilbox
# Time:2022/1/18 9:40


nums1 = [2,2,2,3,4,9,0,0]
nums2 = [1,5,6,10]
m = 5
n = 4
i,j=0,0
while j<n:
    while nums1[i]:
        if nums2[j]<=nums1[i]:
            nums1.insert(i,nums2[j])
            break
        elif (nums2[j]>nums1[i] and nums2[j]<nums1[i+1]) or nums1[i+1]==0:
             nums1.insert(i+1,nums2[j])
             break
        i+=1
    j+=1

