# Task 3: Cross-Domain Machine-Generated Text Detection (RAID)

[![Code License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-green.svg)](https://raw.githubusercontent.com/mbzuai-nlp/SemEval2024-task8/subtask_A_and_B/LICENSE)


<p align="left" float="left">
  <img src="logo.png" height="40" />
</p>


[News](#news) | [Competition](#competition) | [Dataset](#dataset) | [Important Dates](#important_dates) | [Data Format](#data_format) | [Evaluation Metrics](#scorer_and_official_evaluation_metrics) | [Baselines](#baselines) | [Contact](#contact)

Large language models (LLMs) are becoming mainstream and easily accessible, ushering in an explosion of machine-generated content over various channels, such as news, social media, question-answering forums, educational, and even academic contexts. Recent LLMs, such as GPT-4o, Claude3.5 and Gemini1.5-pro, generate remarkably fluent responses to a wide variety of user queries. The articulate nature of such generated texts makes LLMs attractive for replacing human labor in many scenarios. However, this has also resulted in concerns regarding their potential misuse, such as spreading misinformation and causing disruptions in the education system. Since humans perform only slightly better than chance when classifying machine-generated vs. human-written text, there is a need to develop automatic systems to identify machine-generated text with the goal of mitigating its potential misuse. 

## Theme: Cross-Domain Detection
TODO: Write big ol' paragraph here about how detectors need more domain robustness and how open domain API based detectors are becoming the standard. We don't know what form text will be in and it's well established that many detectors have holes across multiple domains. 

In the COLING Workshop on MGT Detection Task 3, we focus on **cross-domain robustness** of detectors. We adopt the same straightforward binary problem formulation as Task 1 however we include texts from 8 different domains. 

These domains are:

| Domain              | Source | Dataset Link |
| :---------------- | :------: | :----: |
| Arxiv Abstracts | [arxiv.org](https://arxiv.org) | [(Link)](https://www.kaggle.com/datasets/Cornell-University/arxiv) |
| Book Plot Summaries | [wikipedia.org](https://wikipedia.org) | [(Link)](https://paperswithcode.com/dataset/cmu-book-summary-dataset) |
| BBC News Articles |  [bbc.com/news](https://www.bbc.com/news) | [(Link)](https://github.com/derekgreene/bbc-datasets) |
| Poems |  [poemhunter.com](https://www.poemhunter.com/)   | [(Link)](https://www.kaggle.com/datasets/michaelarman/poemsdataset) |
| Reddit Posts | [reddit.com](https://www.reddit.com/) | [(Link)](https://huggingface.co/datasets/sentence-transformers/reddit-title-body) |
| Recipes | [allrecipes.com](https://www.allrecipes.com/) | [(Link)](https://recipenlg.cs.put.poznan.pl/) |
| IMDb Movie Reviews | [imdb.com](https://www.imdb.com/) | [(Link)](https://ieee-dataport.org/open-access/imdb-movie-reviews-dataset) |
| Wikipedia Articles | [wikipedia.org](https://www.wikipedia.org/) | [(Link)](https://huggingface.co/datasets/aadityaubhat/GPT-wiki-intro) |

<!-- [cookbooks.com](https://cookbooks.com/), [food.com](https://www.food.com/), [yummly.com](https://www.yummly.com/) -->

There are two subtasks:
- Subtask A: Non-Adversarial Cross-Domain MGT detection.
- Subtask B: Adversarial Cross-Domain MGT detection.

## NEWS 

### 18 Sep 2024

We have released our instructions and training set.

## Competition

The competition will be held on the RAID website:
- [RAID Website](https://raid-bench.xyz/)
- Competition Leaderboard (TBD)

## <a name="dataset"></a>Dataset
For this task we will be using the RAID dataset as well as an extra selection of human-written data.
**Download RAID** by consulting the [RAID Github Repository](https://github.com/liamdugan/raid?tab=readme-ov-file#download-raid)
We will release the extra selection of human-written data soon.

## <a name="important_dates"></a>Important Dates

- 18th September, 2024: Training set release
- 20th October, 2024: Test set release and evaluation phase starts
- 25th October, 2024: Evaluation phase closes
- 28th October, 2024: Leaderboard to be public
- 15th November, 2024: System description paper submission

## <a name="data_format"></a>Prediction File Format and Format Checkers
TODO

## <a name="scorer_and_official_evaluation_metrics"></a>Scorer and Official Evaluation Metrics

The **official evaluation metric** is **TPR @ FPR=5%**. 

## <a name="baselines"></a>Baselines
TODO

## <a name="contact"></a>Contact

Website: [https://genai-content-detection.gitlab.io](https://genai-content-detection.gitlab.io)  
Email: genai-content-detection@googlegroups.com
