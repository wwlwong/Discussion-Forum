import { Link } from "react-router-dom";
import "./styles.css";

const PostCard = ({ post }) => {
  const { title, id } = post;

  return (
    <li className="post-card" id={id}>
      <Link to={`/post/${id}`}>
        <div>
          <h2>{title}</h2>
        </div>
      </Link>
    </li>
  );
};
export default PostCard;