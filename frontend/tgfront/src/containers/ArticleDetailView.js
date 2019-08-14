import React from "react";
import axios from "axios";
import { Card, Button } from "antd";
import CustomForm from "../components/Form";
class ArticleDetailView extends React.Component {
  state = {
    article: {}
  };

  componentDidMount() {
    const articleID = this.props.match.params.articleID;
    axios.get("http://127.0.0.1:8000/api/" + articleID).then(res => {
      this.setState(
        {
          article: res.data
        },
        () => {
          console.log(res.data);
          console.log("sss");
        }
      );
    });
  }
  handleDelete() {
    const articleID = this.props.match.params.articleID;
    axios.delete("http://127.0.0.1:8000/api/" + articleID);
    this.props.history.push("/)");
    this.forceUpdate();
  }
  render() {
    return (
      <div>
        <Card title={this.state.article.title}>
          <p>{this.state.article.content}</p>
        </Card>
        <CustomForm
          requestType="put"
          articleID={this.props.match.params.articleID}
          btnText="Update"
        />
        <form onSubmit={this.handleDelete}>
          <Button htmlType="submit" type="danger">
            Delete
          </Button>
        </form>
      </div>
    );
  }
}

export default ArticleDetailView;
