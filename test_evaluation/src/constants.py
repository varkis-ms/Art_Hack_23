TEST_GENERATOR_PROMPT = """
Create {num_questions} different questions about given article.You should create questions using russian language.

Text of this article:
{article_text}

For each question calculate popularity from 1 to 10.
For each question calculate difficulty from 1 to 10.

Write each question with popularity and difficulty. Also write answer for this question using text of given article.
Provide this output on new line with given format:
<Q>question</Q><P>popularity</P><D>difficulty</D><A>answer</A>
"""
