try:
    import cStringIO as StringIO
except ImportError:
    import StringIO
from django.http import HttpResponse
from xlsxwriter.workbook import Workbook
import xlsxwriter
import pandas as pd
import numpy as np
import os
import re
import sys

def hello(request):
  df2 = pd.DataFrame(np.random.randn(5, 10))

  myPage = """
        
<!DOCTYPE html>
<html>
<head>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
<script>
$(document).ready(function(){
  $("button").click(function(){
    $("#123").hide();
  });
});
</script>
</head>

<body>
<h2>This is a heading</h2>
<p id = "123">This is a paragraph.</p>
<p>This is another paragraph.</p>
<button>Click me</button>
</body>
</html>

          """
  return HttpResponse(myPage)

def helloworld(request):
	return HttpResponse("it worked!")

def hellothere(request):
  return HttpResponse("woohoo")