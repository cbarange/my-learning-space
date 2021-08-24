---
sidebar_position: 1
---

# HTML

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
    <meta name="viewport" content="width=device-width"> <!-- this forces mobile browsers to adopt their real viewport width for loading web pages (some mobile browsers lie about their viewport width, and instead load pages at a larger viewport width then shrink the loaded page down, which is not very helpful for responsive images or design).-->

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

### Content structure


```xml
<ul> <!-- Unordered -->
  <li>milk</li>
  <li>eggs</li>
</ul>

<ol> <!-- Ordered -->
  <li>Drive to the end of the road</li>
  <li>Turn right</li>
</ol>

<!-- Emphasis and importance -->
<span>  </span> <!-- highlight some word -->
<i>  </i> <!-- highlight some letter -->
<em> </em> <!-- highlight one word -->
<b> </b> <!-- bold word --> 
<strong> </strong> <!-- bold text -->
<u> </u> <!-- underline -->
<!-- eg -->
<p> On <strong>Sunday January 9th 2010</strong>, a gang of <em>goths</em> were spotted [...] <span>If anyone has <strong>any</strong> information about this incident, <b>please</b> contact the police <strong>now</strong>.</span> <i>see you soon</i>></p>

<!-- hyperlink -->
<a href="https://www.mozilla.org/en-US/" title="Tooltips when mouse hover">the Mozilla homepage</a>
<a href="https://mozilla.org/"> <img src="mozilla-image.png" alt="mozilla logo link to home page"></a>
<!-- same directory href="contacts.html" -->
<!-- Moving down into subdirectories href="projects/index.html" -->
<!-- Moving back up into parent directories href="../pdfs/project-brief.pdf" -->

<!-- Document fragments -->
<h2 id="Mailing_address">Mailing address</h2>
<a href="#Mailing_address">mail</a>
<a href="contacts.html#Mailing_address">mail</a> <!-- anchor on other page -->


<a href="https://download.mozilla.org/" download="firefox-latest-64bit-installer.exe">Download</a>
<a href="mailto:nowhere@mozilla.org">Send email to nowhere</a>
<a href="mailto:nowhere@mozilla.org?cc=name2@rapidtables.com&bcc=name3@rapidtables.com&subject=The%20subject%20of%20the%20email&body=The%20body%20of%20the%20email">Send mail with cc, bcc, subject and body</a>
<a href="tel:123-456-7890">CLICK TO CALL</a>
<a href="skype:555-666-7777">555-666-7777</a>. 


<!-- absolute URL: Points to a location defined by its absolute location on the web, including protocol and domain name. -->
<!-- relative URL: Points to a location that is relative to the file you are linking from -->
<!-- Use relative wherever possible -->

<br/> <!-- Do not use <br> to create margins between paragraphs; wrap them in <p> elements and use the CSS margin property to control their size. -->
```

### Image

```xml

```


### Form

### 