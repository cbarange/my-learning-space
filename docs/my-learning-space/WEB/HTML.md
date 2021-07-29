# HTML


`data:text/html;base64,PGgxPkhleSAhPC9oMT4=`
https://developer.mozilla.org/fr/docs/Web/HTTP/Basics_of_HTTP/Data_URIs

```html
<!DOCTYPE html>
<title>My Example</title>

<div style="border:1px solid black;height:100px;width:140px;overflow-y:hidden;overflow-x:scroll;">
<p style="width:250%;">
By using overflow-x, we can create scroll bars when the contents of this div are wider than the container. By setting this paragraph to 200 percent, it is 200 percent wider than the parent container - forcing an overflow. 
</p>
</div>
```


## Common usage of html
> docs : https://developer.mozilla.org/en-US/docs/Learn

### index.html file
```xml
<!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset="utf-8">
    <meta name="author" content="Here your name">
    <meta name="description" content="This will appear under search engines results">

    <!-- Open Graph, used for previsualisation by socials networks and others -->
    <meta property="og:title" content="site_title">
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="site_name">
    <meta property="og:url" content="https://here_url_of_website.com">
    <meta property="og:image" content="https://url_to_your_logo.png">
    <meta property="og:description" content="site_description">
    <!-- Twitter tag: https://developer.twitter.com/en/docs/twitter-for-websites/cards/overview/abouts-cards -->
    <meta name="twitter:title" content="site_title_twitter">
    <!-- Change mobile browser color interface -->
    <meta name="theme-color" content="#2196F3">

    <!-- Import --> 
    <link rel="icon" href="favicon.ico" type="image/x-icon">
    <link rel="stylesheet" href="my-css-file.css">
    <script src="my-js-file.js" defer></script> <!-- defer instructs the browser to load js after finished parsing html -->

    <title>title of tab</title>
  </head>
  <body>
    <p>This is my page</p>

    <p>Japanese example: <span lang="ja">ご飯が熱い。</span>.</p>

    <h1></h1> <!-- <h1> represents the main heading (use single h1 per page), <h2> represents subheadings, <h3> represents sub-subheadings, avoid to use more than 3 different heading level per page -->

  </body>
</html>
```

### Form

### 