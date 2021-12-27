import "./header.css";

export default function Header() {
  return (
    <div className="header">
      <div className="headerTitles">
        <span className="headerTitleLg">DocTalk Blog</span>
      </div>
      <img
        className="headerImg"
        src="https://www.cedars-sinai.org/content/dam/cedars-sinai/blog/2021/11/why-vaccine-boosters.jpg"
        alt=""
      />
    </div>
  );
}
