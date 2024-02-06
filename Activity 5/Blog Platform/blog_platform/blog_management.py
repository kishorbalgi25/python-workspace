# i.      create_post(title, content, author): Accepts post details and author information, creates a new blog post, and returns the post object.
# ii.      get_post(post_id): Accepts a post ID and returns the details of a specific blog post.
# iii.      list_posts(): Returns a list of all blog posts.

blogs = {}

class Blog:
    id = 1
    
    def __init__(self,title,content,author):
        self.id = __class__.id
        self.title = title
        self.content = content
        self.author = author
        __class__.id+=1
        
# Create Post
def create_post(title,content, author):
    newpost = Blog(title,content,author)
    
    blogs.update({str(newpost.id): newpost})
    
    return newpost

# Get post by ID:
def get_post(post_id):
    if post_id not in blogs:
        print(f"Post with id {post_id} not found")
    
    post = blogs[post_id]
    
    return post

# List posts:
def get_all_posts():
    posts = []
    
    for post in blogs.values():
        posts.append({
            "title": post.title,
            "content": post.content,
            "author": post.author,
        })
        
    return posts