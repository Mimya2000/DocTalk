import Post from "../post/Post";
import "./posts.css";

export default function Posts() {
  return (
    <div className="posts">
      <Post img="https://www.cedars-sinai.org/content/dam/cedars-sinai/blog/2021/10/stem-cell-science.jpg" />
      <Post img="https://www.cedars-sinai.org/content/dam/cedars-sinai/blog/2021/10/myths-facts-adult-congenital-heart-disease.jpg" />
      <Post img="https://www.cedars-sinai.org/content/dam/cedars-sinai/blog/2021/9/radiation-therapy-for-prostate-cancer.jpg" />
      <Post img="https://www.cedars-sinai.org/content/dam/cedars-sinai/blog/2021/10/hip-knee-replacement-surgery-breakthroughs.jpg" />
      <Post img="https://www.cedars-sinai.org/content/dam/cedars-sinai/blog/2021/10/new-aspirin-recommendation.jpg" />
      <Post img="https://www.cedars-sinai.org/content/dam/cedars-sinai/blog/2021/10/when-use-sleep-aids.jpg" />
    </div>
  );
}
