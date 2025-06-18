class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        n=len(nums1)
        answer=[0]*n
        st=[0]*n
        for i in range(n):
            nums1[i]=[nums1[i],i]
        nums1.sort()
        for i in range(n):
            l=nums1[i][1]
            g=nums1[i][0]
            st[i]=[l]
            for j in range(i):
                if nums1[j][0]!=g:
                    st[i].append(nums1[j][1])
        st.sort()
        for i in range(n):
            nums2[i]=[nums2[i],i]
        nums2.sort(reverse=True)
        for i in range(n):
            o=0
            for j in range(n):
                if o>=k:
                    break
                else:
                    if nums2[j][1] in st[i][1:]:
                        answer[i]+=nums2[j][0]
                        o+=1
        return answer