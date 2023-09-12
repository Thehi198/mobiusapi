// simple JS API displays "hello world"

export async function GET(Request) {
    return new Response("hello from javascript", {
        headers: { "content-type": "text/plain" },
    });
}