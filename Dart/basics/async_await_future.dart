void main() async {
    // Futures --> like promises in JS
    // can have uncompleted or completed state
    // can be awaited

    fetchPost().then((post) => print(post));

    final data = await fetchPost();
    print(data);
}

Future<Post> fetchPost() async {
    const delay = Duration(seconds: 3);

    return Future.delayed(delay, () => Post("Guille", 1));
}

class Post {
    String title;
    int userId;

    Post(this.title, this.userId);

    @override
    String toString() {
        return "$title : $userId"; // Custom string representation
    }
}