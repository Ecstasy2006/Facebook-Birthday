Objective : To post Thanks message on your facebook wall when someone posts Happy Birthday Message 
			on your wall.

Please use Graph explorere to lean about facebook's Graph APIs
http://bit.ly/1CTFXZj

To obtain Access token:
On the link above press Get access token button. Select appropriate permissions and then click on get access token.
Make sure that you select extended permission->publish actions.
For faster development I selected all then permissions mentioned there and then gave permission to use my data.
I am not worried as I am the only one to use this token and these tokens are valid only for certain time.(approx 2 hrs)

Future Enhancements:
1: When somebody's posts on your wall, taken his nme and genetate personalized message to thank him/her.
I did this code but some of the friends in my list has restricted access so Graph APIs resulted exception regarding them
and for all others gave me correct name information. Need to find better to find name of the person who posts on your wall.

2: Create personalized message in their preferred language.
Take locale / language info of the person posting on your wall and then create special thanks message in that language.

3: Post some nice thanks image on to wall as a reply.