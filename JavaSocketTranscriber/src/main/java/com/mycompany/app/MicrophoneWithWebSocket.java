package com.mycompany.app;

import java.io.PrintWriter;
import java.net.Socket;

import javax.sound.sampled.AudioFormat;
import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.DataLine;
import javax.sound.sampled.TargetDataLine;

import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import com.ibm.watson.developer_cloud.http.HttpMediaType;
import com.ibm.watson.developer_cloud.speech_to_text.v1.SpeechToText;
import com.ibm.watson.developer_cloud.speech_to_text.v1.model.RecognizeOptions;
import com.ibm.watson.developer_cloud.speech_to_text.v1.model.SpeechResults;
import com.ibm.watson.developer_cloud.speech_to_text.v1.websocket.BaseRecognizeCallback;

/**
 * Recognize microphone input speech continuously using WebSockets.
 */
public class MicrophoneWithWebSocket {

	static Socket socket;
	static PrintWriter out;

	public static void main(final String[] args) throws Exception {
		String hostName = "localhost";
		int portNumber = 8080;
		socket = new Socket(hostName, portNumber);
		out = new PrintWriter(socket.getOutputStream(), true);

		SpeechToText service = new SpeechToText();
		service.setUsernameAndPassword("6c87f806-d875-4458-84c7-0d9b0801f752", "UAFK0sUt5YNT");

		// Signed PCM AudioFormat with 16kHz, 16 bit sample size, mono
		int sampleRate = 16000;
		AudioFormat format = new AudioFormat(sampleRate, 16, 1, true, false);
		DataLine.Info info = new DataLine.Info(TargetDataLine.class, format);

		if (!AudioSystem.isLineSupported(info)) {
			System.out.println("Line not supported");
			System.exit(0);
		}

		TargetDataLine line = (TargetDataLine) AudioSystem.getLine(info);
		line.open(format);
		line.start();

		AudioInputStream audio = new AudioInputStream(line);

		RecognizeOptions options = new RecognizeOptions.Builder().continuous(true).interimResults(true)
				.timestamps(false).wordConfidence(false)
				// .inactivityTimeout(5) // use this to stop listening when the
				// speaker pauses, i.e. for 5s
				.contentType(HttpMediaType.AUDIO_RAW + "; rate=" + sampleRate).build();

		service.recognizeUsingWebSocket(audio, options, new BaseRecognizeCallback() {
			@Override
			public void onTranscription(SpeechResults speechResults) {
				JsonParser jsonParser = new JsonParser();
				JsonObject jObj = jsonParser.parse(speechResults.toString()).getAsJsonObject();
				boolean finalized = jObj.get("results").getAsJsonArray().get(0).getAsJsonObject().get("final")
						.getAsBoolean();
				if (finalized) {
					String transcript = jObj.get("results").getAsJsonArray().get(0).getAsJsonObject()
							.get("alternatives").getAsJsonArray().get(0).getAsJsonObject().get("transcript")
							.getAsString();
					out.println(transcript.substring(0, transcript.length() - 1));
					System.out.println(transcript.substring(0, transcript.length() - 1));
				}
				// System.out.println(speechResults);
			}
		});

		// Run forever
		Thread.sleep(Long.MAX_VALUE);

		// closing the WebSockets underlying InputStream will close the
		// WebSocket itself.
		line.stop();
		line.close();

		System.out.println("End");
	}
}