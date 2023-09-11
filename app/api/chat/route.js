// simple JS API displays "hello world"

export async function GET(Request) {
    return new Response("hello world", {
        headers: { "content-type": "text/plain" },
    });
}

// Path: app/api/server/route.js