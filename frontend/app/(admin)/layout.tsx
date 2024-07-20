import type { Metadata } from "next";
import { Roboto_Flex } from "next/font/google";
import "../globals.css";
import LoginNav from "./LoginNav";

const inter = Roboto_Flex({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Kumbi Trace",
  description: "The People's Baraza",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <head>
        <link rel="icon" href="/fist-up.png" sizes="any" />
      </head>
      <body className={inter.className}>
        <LoginNav/>
        {children}
      </body>
    </html>
  );
}
