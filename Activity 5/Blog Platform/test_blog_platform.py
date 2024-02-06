from blog_platform.user_management import create_user, delete_user
from blog_platform.blog_management import create_post, get_post, get_all_posts
from blog_platform.comment_management import add_comment,get_comments

def main():
    print("Welcome to Blof Platform:")
    print("1. Create a user")
    print("2. Delete a user")
    print("3. Create a post")
    print("4. Get a post by ID")
    print("5. Get all posts")
    print("6. Add a comment")
    print("7. Get all comments of a post")
    print("8. Exit")
    
    
    while(True):
        choice = int(input("Enter your choice: ")) 
        
        if choice == 1:
            username = input("Enter user name: ")
            email = input("Enter email: ")
            user = create_user(username,email)
            print(f"User details: id -> {user.id} username -> {user.username} email -> {user.email}")
            
        elif choice == 2:
            user_id = input("Enter id of user to be deleted: ")
            
            delete_user(user_id)
        elif choice == 3:
            title = input("Enter the title: ")
            content = input("Enter the content: ")
            author = input("Enter the author: ")
            
            post= create_post(title,content,author)
            
            print(f"New Post: id -> {post.id} title -> {post.title} content -> {post.content} author -> {post.author}")
        elif choice == 4:
            post_id = input("Enter id of post: ")
            
            post = get_post(post_id)
            
            print(f"New Post: id -> {post.id} title -> {post.title} content -> {post.content} author -> {post.author}")
        elif choice == 5:
            posts = get_all_posts()
            
            print(posts)
        elif choice == 6:
            post_id  =  input("Enter the post_id: ")
            author = input("Enter the author: ")
            content = input("Enter the content: ")
            comment = add_comment(post_id,author,content)
            
            print("Comment added")
        elif choice == 7:
            post_id = input("Enter the post id: ")
            comments = get_comments(post_id)
            
            print(comments)
        elif choice==8:
            print("Exiting system")
        else:
            print("Invalid choice!")
            
if __name__=="__main__":
    main()