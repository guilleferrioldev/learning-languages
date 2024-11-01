import "dart:convert" as convert;
import "package:http/http.dart" as http;

void main() async {
    fetchPost().then((post) => print(post));
}

fetchPost() async {
    try {
        var uri = Uri.parse("https://jsonplaceholder.typicode.com/posts/1");
        final response = await http.get(uri);
    
        if (response.statusCode == 200) {
            return response.body;
        }
    } catch (e) {
        print(e);
    }

}