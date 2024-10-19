from django.http import HttpResponse, JsonResponse
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import MessageMediaPhoto
from rest_framework.views import APIView
from telegram.models import Article,Category
from .serializers import ArticleSerializer,CategorySerializer


# API credentials
api_id = '24776953'     # Replace with your API ID
api_hash = '50a1f252e8e05df3a771666cbbe7a39c'  # Replace with your API hash
phone_number = '+201015881141' # Your Telegram phone number

# Target channel and user
channel_username = 'testing_awsabry'  # The channel where the messages are posted

async def get_user_messages(request, channel_username):
    """
    This view retrieves all messages from a specific user in a Telegram channel.
    The channel username and user ID are passed as URL parameters.
    """
    try:
        # Connect to Telegram
        async with TelegramClient(phone_number, api_id, api_hash) as client:
            # Get the channel entity
            channel = await client.get_entity(channel_username)
            
            # Fetch messages from the channel
            messages = await client(GetHistoryRequest(
                peer=channel,
                offset_id=0,
                offset_date=None,
                add_offset=0,
                limit=1000,
                max_id=0,
                min_id=0,
                hash=0
            ))

            # Prepare the data for JSON response, filtering out messages with null or empty text
            messages_list = []
            for message in messages.messages:
                if message.message:  # Only include messages with non-null and non-empty text
                    # Check if the message contains a photo
                    photo_url = None
                    if isinstance(message.media, MessageMediaPhoto):
                        # Download the photo and get the file path
                        photo_url = await client.download_media(message.media,)
                    
                    messages_list.append({
                        'id': message.id,
                        'text': message.message,  # Text is guaranteed to be non-null here
                        'photo': photo_url,  # Include the photo file path or None
                        'date': message.date.strftime('%Y-%m-%d %H:%M:%S'),  # Format the date
                    })

            # Filter messages from the specific user
            print(messages)
            # Render messages in a simple template
            return JsonResponse({'messages': messages_list}, safe=False)
    
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}", status=500)



# Get All articles
class get_articles(APIView):
    def get(self,request):
        all = Article.objects.all()
        serializer = ArticleSerializer(all,many = True)
        return JsonResponse({"Names": serializer.data}, safe=False)
    
    # Add Post Request
    def post(request):
        pass
    
# Get All articles
class get_categories(APIView):

    def get(self,request):
        all = Category.objects.all()
        serializer = CategorySerializer(all,many = True)
        return JsonResponse({"Names": serializer.data}, safe=False)
    
    # Add Post Request
    def post(request):
        pass
    
    # Add endpoint to get the articles based on category