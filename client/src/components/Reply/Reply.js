import React, { useState } from "react";

const Reply = ({reply, onDeleteReply, onEditReply}) => {
    const {id, content, created_at, updated_at} = reply;

    function handleDeleteReplyClick(){
        onDeleteReply(id);
    }

    function handleEditReplyClick(){
        onEditReply(id);
    }

    return (
        <div>
            <div className="reply">
                <p>comment ID: {id}</p>
                <p>{content} </p>
                <p>Replied on: {created_at}</p>
            </div>

            <div className='bottomblock'>
                <button className='reply-delete' onClick={handleDeleteReplyClick}>Delete Reply</button>
                <button className='reply-edit' onClick={handleEditReplyClick}>Edit Reply</button>

            </div>


        </div>
        
    )


}

export default Reply