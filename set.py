# user_list=[101,102,103,104,105]
# for user in requests:
#     if user in set(user_list):
#         process_user(user)




team_a={"john","mary","bob"}
team_b={"mary","alice","bob"}
team_c={"bob","charlie","david"}
all_members=team_a | team_b | team_c
common_all=team_a & team_b & team_c
print(f"{len(all_members)},{len(common_all)}")


#removing duplicates from the list
numbers=[1,2,2,3,4,4,5,1]
unique_numbers=list(set(numbers))
print(unique_numbers)


#finding common elements
online_customers={101,102,103,105,107}
retail_customers={102,104,105,106}
cross_channel_customers=online_customers & retail_customers
print(f"cross_channel_customers:{cross_channel_customers}")



#finding difference between datasets
expected_items={"laptop","mouse","keyboard","monitor","webcam"}
acutal_items={"laptop","keyboard","monitor","printer"}
missing_items=expected_items - acutal_items
print(f"missing fromthe inventory:{missing_items}")


#symmetric difference
morning_attendees={"alice","bob","charlie","david"}
evening_attendees={"charlie","david","eve","frank"}
single_session=morning_attendees ^ evening_attendees
print(f"single session attendees:{single_session}")
both_session=morning_attendees & evening_attendees
print(f"both session:{both_session}")


#union operations for data
insta_followers={"user1","user2","user3","user4"}
twitter_followers={"user3"."user4","user5","user6"}
all_followers=insta_followers | twitter_followers
print(f"total unique followers:{len(all_followers)}")
all_followers=insta_followers.union(twitter_followers)
print(f"all followers:{all_followers}")


#fast membership testing
allowed_extensions={"jpg","jpeg","png","gif"}
print(f"is gif allowed ? {gif in allowed_extensions}")