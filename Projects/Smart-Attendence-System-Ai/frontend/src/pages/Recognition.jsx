import React, { useRef, useState, useCallback } from 'react';
import { recognizeAndMark } from '../services/api';

const Recognition = () => {
    const videoRef = useRef(null);
    const canvasRef = useRef(null);
    const [stream, setStream] = useState(null);
    const [loading, setLoading] = useState(false);
    const [result, setResult] = useState(null);

    const startCamera = async () => {
        try {
            const mediaStream = await navigator.mediaDevices.getUserMedia({ video: true });
            setStream(mediaStream);
            if (videoRef.current) {
                videoRef.current.srcObject = mediaStream;
            }
        } catch (err) {
            setResult({ type: 'error', text: 'Camera access denied or unavailable.' });
        }
    };

    const stopCamera = () => {
        if (stream) {
            stream.getTracks().forEach(track => track.stop());
            setStream(null);
        }
    };

    const captureAndRecognize = () => {
        if (!videoRef.current || !canvasRef.current) return;
        
        const video = videoRef.current;
        const canvas = canvasRef.current;
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        
        const ctx = canvas.getContext('2d');
        ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
        
        canvas.toBlob(async (blob) => {
            if (!blob) return;
            setLoading(true);
            setResult(null);
            
            try {
                const res = await recognizeAndMark(blob);
                if (res.data.status === 'success') {
                    if (res.data.attendance_status === 'duplicate') {
                        setResult({ type: 'info', text: res.data.message });
                    } else {
                        setResult({ 
                            type: 'success', 
                            text: `Recognized ${res.data.student_name} (${res.data.confidence}% match). ${res.data.message}` 
                        });
                    }
                } else {
                    setResult({ type: 'error', text: res.data.message || 'Recognition failed.' });
                }
            } catch (err) {
                setResult({ type: 'error', text: err.response?.data?.detail || err.message });
            } finally {
                setLoading(false);
            }
        }, 'image/jpeg', 0.8);
    };

    // Cleanup on unmount
    React.useEffect(() => {
        return () => stopCamera();
    }, []);

    return (
        <div>
            <div className="page-header">
                <h1 className="page-title">Live Face Recognition</h1>
                <p>Start the camera to identify students and mark attendance.</p>
            </div>

            <div style={{display: 'flex', gap: '24px', alignItems: 'flex-start'}}>
                <div className="camera-container" style={{flex: 1}}>
                    <div style={{background: '#000', borderRadius: '8px', overflow: 'hidden', marginBottom: '24px'}}>
                        <video 
                            ref={videoRef} 
                            autoPlay 
                            playsInline 
                            style={{width: '100%', display: stream ? 'block' : 'none'}}
                        />
                        {!stream && (
                            <div style={{height: '400px', display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#666', background: '#f8fafc'}}>
                                Camera is off
                            </div>
                        )}
                    </div>
                    
                    <canvas ref={canvasRef} style={{display: 'none'}} />
                    
                    <div style={{display: 'flex', gap: '16px', justifyContent: 'center'}}>
                        {!stream ? (
                            <button className="btn" onClick={startCamera}>Start Camera</button>
                        ) : (
                            <button className="btn" style={{backgroundColor: '#dc2626'}} onClick={stopCamera}>Stop Camera</button>
                        )}
                        <button className="btn" disabled={!stream || loading} onClick={captureAndRecognize}>
                            {loading ? 'Processing...' : 'Capture & Mark'}
                        </button>
                    </div>

                    {result && (
                        <div className={`alert alert-${result.type}`}>
                            {result.text}
                        </div>
                    )}
                </div>

                <div className="table-container" style={{flex: 1, padding: '24px'}}>
                    <h3 style={{marginBottom: '16px'}}>Instructions</h3>
                    <ul style={{lineHeight: '1.8', color: '#475569', paddingLeft: '20px'}}>
                        <li>Ensure good lighting in the room.</li>
                        <li>Face the camera directly.</li>
                        <li>Click <strong>Start Camera</strong> to begin the feed.</li>
                        <li>Click <strong>Capture & Mark</strong> when the student is clearly visible.</li>
                        <li>If the student is already marked present for today, the system will notify you without creating a duplicate record.</li>
                    </ul>
                </div>
            </div>
        </div>
    );
};

export default Recognition;
