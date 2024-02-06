# a.       add_comment(post_id, author, content): Accepts post details, author information, and comment content, adds a new comment to a post, and returns the comment object.

# b.      get_comments(post_id): Accepts a post ID and returns a list of comments for that post.

class Comment:
    id = 1 
    
    def __init__(self, post_id, author, content):
        self.id = __class__.id
        self.post_id = post_id
        self.author = author
        self.content = content
        __class__.id +=1
        
        
comments = {}
# Add comment:
def add_comment(post_id,author,content):
    newComment = Comment(post_id,author,content)
    
    comments.update({str(newComment.id):newComment})
    
    return newComment

# Get Comments:
def get_comments(post_id):
    filtered_comments = list(filter(lambda comment: comment.post_id==post_id,comments.values()))
    all_comments = map(lambda comment : {"post_id":comment.post_id,"author":comment.author,"content":comment.content},filtered_comments)
    
    return list(all_comments)
